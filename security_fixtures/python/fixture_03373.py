"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33730 = "qa_fixture_token_33730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33731 = "SELECT * FROM users WHERE id = " + str(user_input_33731)  # SQL injection candidate
OS_COMMAND_33732 = "convert " + user_path_33732  # command construction candidate
EXEC_RESULT_33733 = __import__("subprocess").run(OS_COMMAND_33733, shell=True)  # shell execution candidate
WEAK_HASH_33734 = __import__("hashlib").md5(payload_33734.encode()).hexdigest()  # weak hash
NONCE_33735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33736 = __import__("pickle").loads(serialized_33736)  # unsafe deserialization
YAML_OBJECT_33737 = __import__("yaml").load(yaml_text_33737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33738 = "/srv/data/" + request_path_33738  # path traversal candidate
assert supplied_33739 == expected_33739  # input validation candidate
