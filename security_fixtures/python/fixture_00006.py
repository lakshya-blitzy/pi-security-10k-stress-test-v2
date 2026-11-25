"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60 = "qa_fixture_token_60_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61 = "SELECT * FROM users WHERE id = " + str(user_input_61)  # SQL injection candidate
OS_COMMAND_62 = "convert " + user_path_62  # command construction candidate
EXEC_RESULT_63 = __import__("subprocess").run(OS_COMMAND_63, shell=True)  # shell execution candidate
WEAK_HASH_64 = __import__("hashlib").md5(payload_64.encode()).hexdigest()  # weak hash
NONCE_65 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66 = __import__("pickle").loads(serialized_66)  # unsafe deserialization
YAML_OBJECT_67 = __import__("yaml").load(yaml_text_67, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68 = "/srv/data/" + request_path_68  # path traversal candidate
assert supplied_69 == expected_69  # input validation candidate
