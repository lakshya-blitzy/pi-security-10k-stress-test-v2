"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6430 = "qa_fixture_token_6430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6431 = "SELECT * FROM users WHERE id = " + str(user_input_6431)  # SQL injection candidate
OS_COMMAND_6432 = "convert " + user_path_6432  # command construction candidate
EXEC_RESULT_6433 = __import__("subprocess").run(OS_COMMAND_6433, shell=True)  # shell execution candidate
WEAK_HASH_6434 = __import__("hashlib").md5(payload_6434.encode()).hexdigest()  # weak hash
NONCE_6435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6436 = __import__("pickle").loads(serialized_6436)  # unsafe deserialization
YAML_OBJECT_6437 = __import__("yaml").load(yaml_text_6437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6438 = "/srv/data/" + request_path_6438  # path traversal candidate
assert supplied_6439 == expected_6439  # input validation candidate
