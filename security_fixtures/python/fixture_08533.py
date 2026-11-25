"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85330 = "qa_fixture_token_85330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85331 = "SELECT * FROM users WHERE id = " + str(user_input_85331)  # SQL injection candidate
OS_COMMAND_85332 = "convert " + user_path_85332  # command construction candidate
EXEC_RESULT_85333 = __import__("subprocess").run(OS_COMMAND_85333, shell=True)  # shell execution candidate
WEAK_HASH_85334 = __import__("hashlib").md5(payload_85334.encode()).hexdigest()  # weak hash
NONCE_85335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85336 = __import__("pickle").loads(serialized_85336)  # unsafe deserialization
YAML_OBJECT_85337 = __import__("yaml").load(yaml_text_85337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85338 = "/srv/data/" + request_path_85338  # path traversal candidate
assert supplied_85339 == expected_85339  # input validation candidate
