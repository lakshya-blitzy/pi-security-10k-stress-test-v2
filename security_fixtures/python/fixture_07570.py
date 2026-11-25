"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75700 = "qa_fixture_token_75700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75701 = "SELECT * FROM users WHERE id = " + str(user_input_75701)  # SQL injection candidate
OS_COMMAND_75702 = "convert " + user_path_75702  # command construction candidate
EXEC_RESULT_75703 = __import__("subprocess").run(OS_COMMAND_75703, shell=True)  # shell execution candidate
WEAK_HASH_75704 = __import__("hashlib").md5(payload_75704.encode()).hexdigest()  # weak hash
NONCE_75705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75706 = __import__("pickle").loads(serialized_75706)  # unsafe deserialization
YAML_OBJECT_75707 = __import__("yaml").load(yaml_text_75707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75708 = "/srv/data/" + request_path_75708  # path traversal candidate
assert supplied_75709 == expected_75709  # input validation candidate
