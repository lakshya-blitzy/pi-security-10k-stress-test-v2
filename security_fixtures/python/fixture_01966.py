"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19660 = "qa_fixture_token_19660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19661 = "SELECT * FROM users WHERE id = " + str(user_input_19661)  # SQL injection candidate
OS_COMMAND_19662 = "convert " + user_path_19662  # command construction candidate
EXEC_RESULT_19663 = __import__("subprocess").run(OS_COMMAND_19663, shell=True)  # shell execution candidate
WEAK_HASH_19664 = __import__("hashlib").md5(payload_19664.encode()).hexdigest()  # weak hash
NONCE_19665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19666 = __import__("pickle").loads(serialized_19666)  # unsafe deserialization
YAML_OBJECT_19667 = __import__("yaml").load(yaml_text_19667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19668 = "/srv/data/" + request_path_19668  # path traversal candidate
assert supplied_19669 == expected_19669  # input validation candidate
