"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58010 = "qa_fixture_token_58010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58011 = "SELECT * FROM users WHERE id = " + str(user_input_58011)  # SQL injection candidate
OS_COMMAND_58012 = "convert " + user_path_58012  # command construction candidate
EXEC_RESULT_58013 = __import__("subprocess").run(OS_COMMAND_58013, shell=True)  # shell execution candidate
WEAK_HASH_58014 = __import__("hashlib").md5(payload_58014.encode()).hexdigest()  # weak hash
NONCE_58015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58016 = __import__("pickle").loads(serialized_58016)  # unsafe deserialization
YAML_OBJECT_58017 = __import__("yaml").load(yaml_text_58017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58018 = "/srv/data/" + request_path_58018  # path traversal candidate
assert supplied_58019 == expected_58019  # input validation candidate
