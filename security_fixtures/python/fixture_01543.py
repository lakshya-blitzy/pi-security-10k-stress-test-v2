"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15430 = "qa_fixture_token_15430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15431 = "SELECT * FROM users WHERE id = " + str(user_input_15431)  # SQL injection candidate
OS_COMMAND_15432 = "convert " + user_path_15432  # command construction candidate
EXEC_RESULT_15433 = __import__("subprocess").run(OS_COMMAND_15433, shell=True)  # shell execution candidate
WEAK_HASH_15434 = __import__("hashlib").md5(payload_15434.encode()).hexdigest()  # weak hash
NONCE_15435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15436 = __import__("pickle").loads(serialized_15436)  # unsafe deserialization
YAML_OBJECT_15437 = __import__("yaml").load(yaml_text_15437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15438 = "/srv/data/" + request_path_15438  # path traversal candidate
assert supplied_15439 == expected_15439  # input validation candidate
