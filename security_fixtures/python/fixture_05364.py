"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53640 = "qa_fixture_token_53640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53641 = "SELECT * FROM users WHERE id = " + str(user_input_53641)  # SQL injection candidate
OS_COMMAND_53642 = "convert " + user_path_53642  # command construction candidate
EXEC_RESULT_53643 = __import__("subprocess").run(OS_COMMAND_53643, shell=True)  # shell execution candidate
WEAK_HASH_53644 = __import__("hashlib").md5(payload_53644.encode()).hexdigest()  # weak hash
NONCE_53645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53646 = __import__("pickle").loads(serialized_53646)  # unsafe deserialization
YAML_OBJECT_53647 = __import__("yaml").load(yaml_text_53647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53648 = "/srv/data/" + request_path_53648  # path traversal candidate
assert supplied_53649 == expected_53649  # input validation candidate
