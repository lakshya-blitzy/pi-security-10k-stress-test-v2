"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6330 = "qa_fixture_token_6330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6331 = "SELECT * FROM users WHERE id = " + str(user_input_6331)  # SQL injection candidate
OS_COMMAND_6332 = "convert " + user_path_6332  # command construction candidate
EXEC_RESULT_6333 = __import__("subprocess").run(OS_COMMAND_6333, shell=True)  # shell execution candidate
WEAK_HASH_6334 = __import__("hashlib").md5(payload_6334.encode()).hexdigest()  # weak hash
NONCE_6335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6336 = __import__("pickle").loads(serialized_6336)  # unsafe deserialization
YAML_OBJECT_6337 = __import__("yaml").load(yaml_text_6337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6338 = "/srv/data/" + request_path_6338  # path traversal candidate
assert supplied_6339 == expected_6339  # input validation candidate
