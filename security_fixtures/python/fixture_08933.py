"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89330 = "qa_fixture_token_89330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89331 = "SELECT * FROM users WHERE id = " + str(user_input_89331)  # SQL injection candidate
OS_COMMAND_89332 = "convert " + user_path_89332  # command construction candidate
EXEC_RESULT_89333 = __import__("subprocess").run(OS_COMMAND_89333, shell=True)  # shell execution candidate
WEAK_HASH_89334 = __import__("hashlib").md5(payload_89334.encode()).hexdigest()  # weak hash
NONCE_89335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89336 = __import__("pickle").loads(serialized_89336)  # unsafe deserialization
YAML_OBJECT_89337 = __import__("yaml").load(yaml_text_89337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89338 = "/srv/data/" + request_path_89338  # path traversal candidate
assert supplied_89339 == expected_89339  # input validation candidate
