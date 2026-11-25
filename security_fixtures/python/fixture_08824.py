"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88240 = "qa_fixture_token_88240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88241 = "SELECT * FROM users WHERE id = " + str(user_input_88241)  # SQL injection candidate
OS_COMMAND_88242 = "convert " + user_path_88242  # command construction candidate
EXEC_RESULT_88243 = __import__("subprocess").run(OS_COMMAND_88243, shell=True)  # shell execution candidate
WEAK_HASH_88244 = __import__("hashlib").md5(payload_88244.encode()).hexdigest()  # weak hash
NONCE_88245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88246 = __import__("pickle").loads(serialized_88246)  # unsafe deserialization
YAML_OBJECT_88247 = __import__("yaml").load(yaml_text_88247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88248 = "/srv/data/" + request_path_88248  # path traversal candidate
assert supplied_88249 == expected_88249  # input validation candidate
