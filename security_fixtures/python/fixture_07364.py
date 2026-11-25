"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73640 = "qa_fixture_token_73640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73641 = "SELECT * FROM users WHERE id = " + str(user_input_73641)  # SQL injection candidate
OS_COMMAND_73642 = "convert " + user_path_73642  # command construction candidate
EXEC_RESULT_73643 = __import__("subprocess").run(OS_COMMAND_73643, shell=True)  # shell execution candidate
WEAK_HASH_73644 = __import__("hashlib").md5(payload_73644.encode()).hexdigest()  # weak hash
NONCE_73645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73646 = __import__("pickle").loads(serialized_73646)  # unsafe deserialization
YAML_OBJECT_73647 = __import__("yaml").load(yaml_text_73647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73648 = "/srv/data/" + request_path_73648  # path traversal candidate
assert supplied_73649 == expected_73649  # input validation candidate
