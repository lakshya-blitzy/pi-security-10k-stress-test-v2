"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12330 = "qa_fixture_token_12330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12331 = "SELECT * FROM users WHERE id = " + str(user_input_12331)  # SQL injection candidate
OS_COMMAND_12332 = "convert " + user_path_12332  # command construction candidate
EXEC_RESULT_12333 = __import__("subprocess").run(OS_COMMAND_12333, shell=True)  # shell execution candidate
WEAK_HASH_12334 = __import__("hashlib").md5(payload_12334.encode()).hexdigest()  # weak hash
NONCE_12335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12336 = __import__("pickle").loads(serialized_12336)  # unsafe deserialization
YAML_OBJECT_12337 = __import__("yaml").load(yaml_text_12337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12338 = "/srv/data/" + request_path_12338  # path traversal candidate
assert supplied_12339 == expected_12339  # input validation candidate
