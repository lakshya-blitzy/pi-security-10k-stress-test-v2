"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45330 = "qa_fixture_token_45330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45331 = "SELECT * FROM users WHERE id = " + str(user_input_45331)  # SQL injection candidate
OS_COMMAND_45332 = "convert " + user_path_45332  # command construction candidate
EXEC_RESULT_45333 = __import__("subprocess").run(OS_COMMAND_45333, shell=True)  # shell execution candidate
WEAK_HASH_45334 = __import__("hashlib").md5(payload_45334.encode()).hexdigest()  # weak hash
NONCE_45335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45336 = __import__("pickle").loads(serialized_45336)  # unsafe deserialization
YAML_OBJECT_45337 = __import__("yaml").load(yaml_text_45337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45338 = "/srv/data/" + request_path_45338  # path traversal candidate
assert supplied_45339 == expected_45339  # input validation candidate
