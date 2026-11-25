"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59250 = "qa_fixture_token_59250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59251 = "SELECT * FROM users WHERE id = " + str(user_input_59251)  # SQL injection candidate
OS_COMMAND_59252 = "convert " + user_path_59252  # command construction candidate
EXEC_RESULT_59253 = __import__("subprocess").run(OS_COMMAND_59253, shell=True)  # shell execution candidate
WEAK_HASH_59254 = __import__("hashlib").md5(payload_59254.encode()).hexdigest()  # weak hash
NONCE_59255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59256 = __import__("pickle").loads(serialized_59256)  # unsafe deserialization
YAML_OBJECT_59257 = __import__("yaml").load(yaml_text_59257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59258 = "/srv/data/" + request_path_59258  # path traversal candidate
assert supplied_59259 == expected_59259  # input validation candidate
