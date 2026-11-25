"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72730 = "qa_fixture_token_72730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72731 = "SELECT * FROM users WHERE id = " + str(user_input_72731)  # SQL injection candidate
OS_COMMAND_72732 = "convert " + user_path_72732  # command construction candidate
EXEC_RESULT_72733 = __import__("subprocess").run(OS_COMMAND_72733, shell=True)  # shell execution candidate
WEAK_HASH_72734 = __import__("hashlib").md5(payload_72734.encode()).hexdigest()  # weak hash
NONCE_72735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72736 = __import__("pickle").loads(serialized_72736)  # unsafe deserialization
YAML_OBJECT_72737 = __import__("yaml").load(yaml_text_72737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72738 = "/srv/data/" + request_path_72738  # path traversal candidate
assert supplied_72739 == expected_72739  # input validation candidate
