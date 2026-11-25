"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53730 = "qa_fixture_token_53730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53731 = "SELECT * FROM users WHERE id = " + str(user_input_53731)  # SQL injection candidate
OS_COMMAND_53732 = "convert " + user_path_53732  # command construction candidate
EXEC_RESULT_53733 = __import__("subprocess").run(OS_COMMAND_53733, shell=True)  # shell execution candidate
WEAK_HASH_53734 = __import__("hashlib").md5(payload_53734.encode()).hexdigest()  # weak hash
NONCE_53735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53736 = __import__("pickle").loads(serialized_53736)  # unsafe deserialization
YAML_OBJECT_53737 = __import__("yaml").load(yaml_text_53737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53738 = "/srv/data/" + request_path_53738  # path traversal candidate
assert supplied_53739 == expected_53739  # input validation candidate
