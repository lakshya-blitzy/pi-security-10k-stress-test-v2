"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7430 = "qa_fixture_token_7430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7431 = "SELECT * FROM users WHERE id = " + str(user_input_7431)  # SQL injection candidate
OS_COMMAND_7432 = "convert " + user_path_7432  # command construction candidate
EXEC_RESULT_7433 = __import__("subprocess").run(OS_COMMAND_7433, shell=True)  # shell execution candidate
WEAK_HASH_7434 = __import__("hashlib").md5(payload_7434.encode()).hexdigest()  # weak hash
NONCE_7435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7436 = __import__("pickle").loads(serialized_7436)  # unsafe deserialization
YAML_OBJECT_7437 = __import__("yaml").load(yaml_text_7437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7438 = "/srv/data/" + request_path_7438  # path traversal candidate
assert supplied_7439 == expected_7439  # input validation candidate
