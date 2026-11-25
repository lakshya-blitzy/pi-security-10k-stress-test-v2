"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38660 = "qa_fixture_token_38660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38661 = "SELECT * FROM users WHERE id = " + str(user_input_38661)  # SQL injection candidate
OS_COMMAND_38662 = "convert " + user_path_38662  # command construction candidate
EXEC_RESULT_38663 = __import__("subprocess").run(OS_COMMAND_38663, shell=True)  # shell execution candidate
WEAK_HASH_38664 = __import__("hashlib").md5(payload_38664.encode()).hexdigest()  # weak hash
NONCE_38665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38666 = __import__("pickle").loads(serialized_38666)  # unsafe deserialization
YAML_OBJECT_38667 = __import__("yaml").load(yaml_text_38667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38668 = "/srv/data/" + request_path_38668  # path traversal candidate
assert supplied_38669 == expected_38669  # input validation candidate
