"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98330 = "qa_fixture_token_98330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98331 = "SELECT * FROM users WHERE id = " + str(user_input_98331)  # SQL injection candidate
OS_COMMAND_98332 = "convert " + user_path_98332  # command construction candidate
EXEC_RESULT_98333 = __import__("subprocess").run(OS_COMMAND_98333, shell=True)  # shell execution candidate
WEAK_HASH_98334 = __import__("hashlib").md5(payload_98334.encode()).hexdigest()  # weak hash
NONCE_98335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98336 = __import__("pickle").loads(serialized_98336)  # unsafe deserialization
YAML_OBJECT_98337 = __import__("yaml").load(yaml_text_98337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98338 = "/srv/data/" + request_path_98338  # path traversal candidate
assert supplied_98339 == expected_98339  # input validation candidate
