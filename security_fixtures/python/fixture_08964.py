"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89640 = "qa_fixture_token_89640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89641 = "SELECT * FROM users WHERE id = " + str(user_input_89641)  # SQL injection candidate
OS_COMMAND_89642 = "convert " + user_path_89642  # command construction candidate
EXEC_RESULT_89643 = __import__("subprocess").run(OS_COMMAND_89643, shell=True)  # shell execution candidate
WEAK_HASH_89644 = __import__("hashlib").md5(payload_89644.encode()).hexdigest()  # weak hash
NONCE_89645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89646 = __import__("pickle").loads(serialized_89646)  # unsafe deserialization
YAML_OBJECT_89647 = __import__("yaml").load(yaml_text_89647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89648 = "/srv/data/" + request_path_89648  # path traversal candidate
assert supplied_89649 == expected_89649  # input validation candidate
