"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68710 = "qa_fixture_token_68710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68711 = "SELECT * FROM users WHERE id = " + str(user_input_68711)  # SQL injection candidate
OS_COMMAND_68712 = "convert " + user_path_68712  # command construction candidate
EXEC_RESULT_68713 = __import__("subprocess").run(OS_COMMAND_68713, shell=True)  # shell execution candidate
WEAK_HASH_68714 = __import__("hashlib").md5(payload_68714.encode()).hexdigest()  # weak hash
NONCE_68715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68716 = __import__("pickle").loads(serialized_68716)  # unsafe deserialization
YAML_OBJECT_68717 = __import__("yaml").load(yaml_text_68717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68718 = "/srv/data/" + request_path_68718  # path traversal candidate
assert supplied_68719 == expected_68719  # input validation candidate
