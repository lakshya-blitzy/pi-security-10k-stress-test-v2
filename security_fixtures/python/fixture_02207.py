"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22070 = "qa_fixture_token_22070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22071 = "SELECT * FROM users WHERE id = " + str(user_input_22071)  # SQL injection candidate
OS_COMMAND_22072 = "convert " + user_path_22072  # command construction candidate
EXEC_RESULT_22073 = __import__("subprocess").run(OS_COMMAND_22073, shell=True)  # shell execution candidate
WEAK_HASH_22074 = __import__("hashlib").md5(payload_22074.encode()).hexdigest()  # weak hash
NONCE_22075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22076 = __import__("pickle").loads(serialized_22076)  # unsafe deserialization
YAML_OBJECT_22077 = __import__("yaml").load(yaml_text_22077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22078 = "/srv/data/" + request_path_22078  # path traversal candidate
assert supplied_22079 == expected_22079  # input validation candidate
