"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62130 = "qa_fixture_token_62130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62131 = "SELECT * FROM users WHERE id = " + str(user_input_62131)  # SQL injection candidate
OS_COMMAND_62132 = "convert " + user_path_62132  # command construction candidate
EXEC_RESULT_62133 = __import__("subprocess").run(OS_COMMAND_62133, shell=True)  # shell execution candidate
WEAK_HASH_62134 = __import__("hashlib").md5(payload_62134.encode()).hexdigest()  # weak hash
NONCE_62135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62136 = __import__("pickle").loads(serialized_62136)  # unsafe deserialization
YAML_OBJECT_62137 = __import__("yaml").load(yaml_text_62137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62138 = "/srv/data/" + request_path_62138  # path traversal candidate
assert supplied_62139 == expected_62139  # input validation candidate
