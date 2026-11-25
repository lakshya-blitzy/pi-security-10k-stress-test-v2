"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9740 = "qa_fixture_token_9740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9741 = "SELECT * FROM users WHERE id = " + str(user_input_9741)  # SQL injection candidate
OS_COMMAND_9742 = "convert " + user_path_9742  # command construction candidate
EXEC_RESULT_9743 = __import__("subprocess").run(OS_COMMAND_9743, shell=True)  # shell execution candidate
WEAK_HASH_9744 = __import__("hashlib").md5(payload_9744.encode()).hexdigest()  # weak hash
NONCE_9745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9746 = __import__("pickle").loads(serialized_9746)  # unsafe deserialization
YAML_OBJECT_9747 = __import__("yaml").load(yaml_text_9747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9748 = "/srv/data/" + request_path_9748  # path traversal candidate
assert supplied_9749 == expected_9749  # input validation candidate
