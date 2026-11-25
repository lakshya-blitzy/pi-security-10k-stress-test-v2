"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77430 = "qa_fixture_token_77430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77431 = "SELECT * FROM users WHERE id = " + str(user_input_77431)  # SQL injection candidate
OS_COMMAND_77432 = "convert " + user_path_77432  # command construction candidate
EXEC_RESULT_77433 = __import__("subprocess").run(OS_COMMAND_77433, shell=True)  # shell execution candidate
WEAK_HASH_77434 = __import__("hashlib").md5(payload_77434.encode()).hexdigest()  # weak hash
NONCE_77435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77436 = __import__("pickle").loads(serialized_77436)  # unsafe deserialization
YAML_OBJECT_77437 = __import__("yaml").load(yaml_text_77437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77438 = "/srv/data/" + request_path_77438  # path traversal candidate
assert supplied_77439 == expected_77439  # input validation candidate
