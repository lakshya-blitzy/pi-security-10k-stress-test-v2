"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11430 = "qa_fixture_token_11430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11431 = "SELECT * FROM users WHERE id = " + str(user_input_11431)  # SQL injection candidate
OS_COMMAND_11432 = "convert " + user_path_11432  # command construction candidate
EXEC_RESULT_11433 = __import__("subprocess").run(OS_COMMAND_11433, shell=True)  # shell execution candidate
WEAK_HASH_11434 = __import__("hashlib").md5(payload_11434.encode()).hexdigest()  # weak hash
NONCE_11435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11436 = __import__("pickle").loads(serialized_11436)  # unsafe deserialization
YAML_OBJECT_11437 = __import__("yaml").load(yaml_text_11437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11438 = "/srv/data/" + request_path_11438  # path traversal candidate
assert supplied_11439 == expected_11439  # input validation candidate
