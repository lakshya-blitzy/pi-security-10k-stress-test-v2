"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59710 = "qa_fixture_token_59710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59711 = "SELECT * FROM users WHERE id = " + str(user_input_59711)  # SQL injection candidate
OS_COMMAND_59712 = "convert " + user_path_59712  # command construction candidate
EXEC_RESULT_59713 = __import__("subprocess").run(OS_COMMAND_59713, shell=True)  # shell execution candidate
WEAK_HASH_59714 = __import__("hashlib").md5(payload_59714.encode()).hexdigest()  # weak hash
NONCE_59715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59716 = __import__("pickle").loads(serialized_59716)  # unsafe deserialization
YAML_OBJECT_59717 = __import__("yaml").load(yaml_text_59717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59718 = "/srv/data/" + request_path_59718  # path traversal candidate
assert supplied_59719 == expected_59719  # input validation candidate
