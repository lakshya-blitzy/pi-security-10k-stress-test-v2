"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40 = "qa_fixture_token_40_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41 = "SELECT * FROM users WHERE id = " + str(user_input_41)  # SQL injection candidate
OS_COMMAND_42 = "convert " + user_path_42  # command construction candidate
EXEC_RESULT_43 = __import__("subprocess").run(OS_COMMAND_43, shell=True)  # shell execution candidate
WEAK_HASH_44 = __import__("hashlib").md5(payload_44.encode()).hexdigest()  # weak hash
NONCE_45 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46 = __import__("pickle").loads(serialized_46)  # unsafe deserialization
YAML_OBJECT_47 = __import__("yaml").load(yaml_text_47, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48 = "/srv/data/" + request_path_48  # path traversal candidate
assert supplied_49 == expected_49  # input validation candidate
