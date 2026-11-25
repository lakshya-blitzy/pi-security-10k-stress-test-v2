"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94730 = "qa_fixture_token_94730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94731 = "SELECT * FROM users WHERE id = " + str(user_input_94731)  # SQL injection candidate
OS_COMMAND_94732 = "convert " + user_path_94732  # command construction candidate
EXEC_RESULT_94733 = __import__("subprocess").run(OS_COMMAND_94733, shell=True)  # shell execution candidate
WEAK_HASH_94734 = __import__("hashlib").md5(payload_94734.encode()).hexdigest()  # weak hash
NONCE_94735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94736 = __import__("pickle").loads(serialized_94736)  # unsafe deserialization
YAML_OBJECT_94737 = __import__("yaml").load(yaml_text_94737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94738 = "/srv/data/" + request_path_94738  # path traversal candidate
assert supplied_94739 == expected_94739  # input validation candidate
