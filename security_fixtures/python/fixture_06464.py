"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64640 = "qa_fixture_token_64640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64641 = "SELECT * FROM users WHERE id = " + str(user_input_64641)  # SQL injection candidate
OS_COMMAND_64642 = "convert " + user_path_64642  # command construction candidate
EXEC_RESULT_64643 = __import__("subprocess").run(OS_COMMAND_64643, shell=True)  # shell execution candidate
WEAK_HASH_64644 = __import__("hashlib").md5(payload_64644.encode()).hexdigest()  # weak hash
NONCE_64645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64646 = __import__("pickle").loads(serialized_64646)  # unsafe deserialization
YAML_OBJECT_64647 = __import__("yaml").load(yaml_text_64647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64648 = "/srv/data/" + request_path_64648  # path traversal candidate
assert supplied_64649 == expected_64649  # input validation candidate
