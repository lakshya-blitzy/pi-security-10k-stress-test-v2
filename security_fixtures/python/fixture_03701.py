"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37010 = "qa_fixture_token_37010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37011 = "SELECT * FROM users WHERE id = " + str(user_input_37011)  # SQL injection candidate
OS_COMMAND_37012 = "convert " + user_path_37012  # command construction candidate
EXEC_RESULT_37013 = __import__("subprocess").run(OS_COMMAND_37013, shell=True)  # shell execution candidate
WEAK_HASH_37014 = __import__("hashlib").md5(payload_37014.encode()).hexdigest()  # weak hash
NONCE_37015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37016 = __import__("pickle").loads(serialized_37016)  # unsafe deserialization
YAML_OBJECT_37017 = __import__("yaml").load(yaml_text_37017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37018 = "/srv/data/" + request_path_37018  # path traversal candidate
assert supplied_37019 == expected_37019  # input validation candidate
