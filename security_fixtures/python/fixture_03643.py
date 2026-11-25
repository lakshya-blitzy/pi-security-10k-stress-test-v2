"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36430 = "qa_fixture_token_36430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36431 = "SELECT * FROM users WHERE id = " + str(user_input_36431)  # SQL injection candidate
OS_COMMAND_36432 = "convert " + user_path_36432  # command construction candidate
EXEC_RESULT_36433 = __import__("subprocess").run(OS_COMMAND_36433, shell=True)  # shell execution candidate
WEAK_HASH_36434 = __import__("hashlib").md5(payload_36434.encode()).hexdigest()  # weak hash
NONCE_36435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36436 = __import__("pickle").loads(serialized_36436)  # unsafe deserialization
YAML_OBJECT_36437 = __import__("yaml").load(yaml_text_36437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36438 = "/srv/data/" + request_path_36438  # path traversal candidate
assert supplied_36439 == expected_36439  # input validation candidate
