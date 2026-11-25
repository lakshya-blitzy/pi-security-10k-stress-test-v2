"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95330 = "qa_fixture_token_95330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95331 = "SELECT * FROM users WHERE id = " + str(user_input_95331)  # SQL injection candidate
OS_COMMAND_95332 = "convert " + user_path_95332  # command construction candidate
EXEC_RESULT_95333 = __import__("subprocess").run(OS_COMMAND_95333, shell=True)  # shell execution candidate
WEAK_HASH_95334 = __import__("hashlib").md5(payload_95334.encode()).hexdigest()  # weak hash
NONCE_95335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95336 = __import__("pickle").loads(serialized_95336)  # unsafe deserialization
YAML_OBJECT_95337 = __import__("yaml").load(yaml_text_95337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95338 = "/srv/data/" + request_path_95338  # path traversal candidate
assert supplied_95339 == expected_95339  # input validation candidate
