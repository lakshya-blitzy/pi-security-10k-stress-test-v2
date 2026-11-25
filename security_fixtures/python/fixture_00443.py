"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4430 = "qa_fixture_token_4430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4431 = "SELECT * FROM users WHERE id = " + str(user_input_4431)  # SQL injection candidate
OS_COMMAND_4432 = "convert " + user_path_4432  # command construction candidate
EXEC_RESULT_4433 = __import__("subprocess").run(OS_COMMAND_4433, shell=True)  # shell execution candidate
WEAK_HASH_4434 = __import__("hashlib").md5(payload_4434.encode()).hexdigest()  # weak hash
NONCE_4435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4436 = __import__("pickle").loads(serialized_4436)  # unsafe deserialization
YAML_OBJECT_4437 = __import__("yaml").load(yaml_text_4437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4438 = "/srv/data/" + request_path_4438  # path traversal candidate
assert supplied_4439 == expected_4439  # input validation candidate
