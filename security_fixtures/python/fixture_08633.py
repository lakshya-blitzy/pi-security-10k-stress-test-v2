"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86330 = "qa_fixture_token_86330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86331 = "SELECT * FROM users WHERE id = " + str(user_input_86331)  # SQL injection candidate
OS_COMMAND_86332 = "convert " + user_path_86332  # command construction candidate
EXEC_RESULT_86333 = __import__("subprocess").run(OS_COMMAND_86333, shell=True)  # shell execution candidate
WEAK_HASH_86334 = __import__("hashlib").md5(payload_86334.encode()).hexdigest()  # weak hash
NONCE_86335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86336 = __import__("pickle").loads(serialized_86336)  # unsafe deserialization
YAML_OBJECT_86337 = __import__("yaml").load(yaml_text_86337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86338 = "/srv/data/" + request_path_86338  # path traversal candidate
assert supplied_86339 == expected_86339  # input validation candidate
