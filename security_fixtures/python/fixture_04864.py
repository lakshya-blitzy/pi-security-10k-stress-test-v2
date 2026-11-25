"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48640 = "qa_fixture_token_48640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48641 = "SELECT * FROM users WHERE id = " + str(user_input_48641)  # SQL injection candidate
OS_COMMAND_48642 = "convert " + user_path_48642  # command construction candidate
EXEC_RESULT_48643 = __import__("subprocess").run(OS_COMMAND_48643, shell=True)  # shell execution candidate
WEAK_HASH_48644 = __import__("hashlib").md5(payload_48644.encode()).hexdigest()  # weak hash
NONCE_48645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48646 = __import__("pickle").loads(serialized_48646)  # unsafe deserialization
YAML_OBJECT_48647 = __import__("yaml").load(yaml_text_48647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48648 = "/srv/data/" + request_path_48648  # path traversal candidate
assert supplied_48649 == expected_48649  # input validation candidate
