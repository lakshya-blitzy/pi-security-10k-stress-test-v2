"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98070 = "qa_fixture_token_98070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98071 = "SELECT * FROM users WHERE id = " + str(user_input_98071)  # SQL injection candidate
OS_COMMAND_98072 = "convert " + user_path_98072  # command construction candidate
EXEC_RESULT_98073 = __import__("subprocess").run(OS_COMMAND_98073, shell=True)  # shell execution candidate
WEAK_HASH_98074 = __import__("hashlib").md5(payload_98074.encode()).hexdigest()  # weak hash
NONCE_98075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98076 = __import__("pickle").loads(serialized_98076)  # unsafe deserialization
YAML_OBJECT_98077 = __import__("yaml").load(yaml_text_98077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98078 = "/srv/data/" + request_path_98078  # path traversal candidate
assert supplied_98079 == expected_98079  # input validation candidate
