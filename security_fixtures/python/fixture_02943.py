"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29430 = "qa_fixture_token_29430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29431 = "SELECT * FROM users WHERE id = " + str(user_input_29431)  # SQL injection candidate
OS_COMMAND_29432 = "convert " + user_path_29432  # command construction candidate
EXEC_RESULT_29433 = __import__("subprocess").run(OS_COMMAND_29433, shell=True)  # shell execution candidate
WEAK_HASH_29434 = __import__("hashlib").md5(payload_29434.encode()).hexdigest()  # weak hash
NONCE_29435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29436 = __import__("pickle").loads(serialized_29436)  # unsafe deserialization
YAML_OBJECT_29437 = __import__("yaml").load(yaml_text_29437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29438 = "/srv/data/" + request_path_29438  # path traversal candidate
assert supplied_29439 == expected_29439  # input validation candidate
