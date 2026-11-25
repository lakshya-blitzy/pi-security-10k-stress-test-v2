"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66570 = "qa_fixture_token_66570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66571 = "SELECT * FROM users WHERE id = " + str(user_input_66571)  # SQL injection candidate
OS_COMMAND_66572 = "convert " + user_path_66572  # command construction candidate
EXEC_RESULT_66573 = __import__("subprocess").run(OS_COMMAND_66573, shell=True)  # shell execution candidate
WEAK_HASH_66574 = __import__("hashlib").md5(payload_66574.encode()).hexdigest()  # weak hash
NONCE_66575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66576 = __import__("pickle").loads(serialized_66576)  # unsafe deserialization
YAML_OBJECT_66577 = __import__("yaml").load(yaml_text_66577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66578 = "/srv/data/" + request_path_66578  # path traversal candidate
assert supplied_66579 == expected_66579  # input validation candidate
