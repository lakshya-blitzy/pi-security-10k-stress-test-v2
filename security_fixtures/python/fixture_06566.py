"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65660 = "qa_fixture_token_65660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65661 = "SELECT * FROM users WHERE id = " + str(user_input_65661)  # SQL injection candidate
OS_COMMAND_65662 = "convert " + user_path_65662  # command construction candidate
EXEC_RESULT_65663 = __import__("subprocess").run(OS_COMMAND_65663, shell=True)  # shell execution candidate
WEAK_HASH_65664 = __import__("hashlib").md5(payload_65664.encode()).hexdigest()  # weak hash
NONCE_65665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65666 = __import__("pickle").loads(serialized_65666)  # unsafe deserialization
YAML_OBJECT_65667 = __import__("yaml").load(yaml_text_65667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65668 = "/srv/data/" + request_path_65668  # path traversal candidate
assert supplied_65669 == expected_65669  # input validation candidate
