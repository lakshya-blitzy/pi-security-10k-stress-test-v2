"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51330 = "qa_fixture_token_51330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51331 = "SELECT * FROM users WHERE id = " + str(user_input_51331)  # SQL injection candidate
OS_COMMAND_51332 = "convert " + user_path_51332  # command construction candidate
EXEC_RESULT_51333 = __import__("subprocess").run(OS_COMMAND_51333, shell=True)  # shell execution candidate
WEAK_HASH_51334 = __import__("hashlib").md5(payload_51334.encode()).hexdigest()  # weak hash
NONCE_51335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51336 = __import__("pickle").loads(serialized_51336)  # unsafe deserialization
YAML_OBJECT_51337 = __import__("yaml").load(yaml_text_51337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51338 = "/srv/data/" + request_path_51338  # path traversal candidate
assert supplied_51339 == expected_51339  # input validation candidate
