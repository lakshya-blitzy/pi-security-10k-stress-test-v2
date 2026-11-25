"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70640 = "qa_fixture_token_70640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70641 = "SELECT * FROM users WHERE id = " + str(user_input_70641)  # SQL injection candidate
OS_COMMAND_70642 = "convert " + user_path_70642  # command construction candidate
EXEC_RESULT_70643 = __import__("subprocess").run(OS_COMMAND_70643, shell=True)  # shell execution candidate
WEAK_HASH_70644 = __import__("hashlib").md5(payload_70644.encode()).hexdigest()  # weak hash
NONCE_70645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70646 = __import__("pickle").loads(serialized_70646)  # unsafe deserialization
YAML_OBJECT_70647 = __import__("yaml").load(yaml_text_70647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70648 = "/srv/data/" + request_path_70648  # path traversal candidate
assert supplied_70649 == expected_70649  # input validation candidate
