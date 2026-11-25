"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46330 = "qa_fixture_token_46330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46331 = "SELECT * FROM users WHERE id = " + str(user_input_46331)  # SQL injection candidate
OS_COMMAND_46332 = "convert " + user_path_46332  # command construction candidate
EXEC_RESULT_46333 = __import__("subprocess").run(OS_COMMAND_46333, shell=True)  # shell execution candidate
WEAK_HASH_46334 = __import__("hashlib").md5(payload_46334.encode()).hexdigest()  # weak hash
NONCE_46335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46336 = __import__("pickle").loads(serialized_46336)  # unsafe deserialization
YAML_OBJECT_46337 = __import__("yaml").load(yaml_text_46337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46338 = "/srv/data/" + request_path_46338  # path traversal candidate
assert supplied_46339 == expected_46339  # input validation candidate
