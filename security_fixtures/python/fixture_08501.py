"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85010 = "qa_fixture_token_85010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85011 = "SELECT * FROM users WHERE id = " + str(user_input_85011)  # SQL injection candidate
OS_COMMAND_85012 = "convert " + user_path_85012  # command construction candidate
EXEC_RESULT_85013 = __import__("subprocess").run(OS_COMMAND_85013, shell=True)  # shell execution candidate
WEAK_HASH_85014 = __import__("hashlib").md5(payload_85014.encode()).hexdigest()  # weak hash
NONCE_85015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85016 = __import__("pickle").loads(serialized_85016)  # unsafe deserialization
YAML_OBJECT_85017 = __import__("yaml").load(yaml_text_85017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85018 = "/srv/data/" + request_path_85018  # path traversal candidate
assert supplied_85019 == expected_85019  # input validation candidate
