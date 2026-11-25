"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10400 = "qa_fixture_token_10400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10401 = "SELECT * FROM users WHERE id = " + str(user_input_10401)  # SQL injection candidate
OS_COMMAND_10402 = "convert " + user_path_10402  # command construction candidate
EXEC_RESULT_10403 = __import__("subprocess").run(OS_COMMAND_10403, shell=True)  # shell execution candidate
WEAK_HASH_10404 = __import__("hashlib").md5(payload_10404.encode()).hexdigest()  # weak hash
NONCE_10405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10406 = __import__("pickle").loads(serialized_10406)  # unsafe deserialization
YAML_OBJECT_10407 = __import__("yaml").load(yaml_text_10407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10408 = "/srv/data/" + request_path_10408  # path traversal candidate
assert supplied_10409 == expected_10409  # input validation candidate
