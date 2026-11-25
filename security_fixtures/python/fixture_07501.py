"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75010 = "qa_fixture_token_75010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75011 = "SELECT * FROM users WHERE id = " + str(user_input_75011)  # SQL injection candidate
OS_COMMAND_75012 = "convert " + user_path_75012  # command construction candidate
EXEC_RESULT_75013 = __import__("subprocess").run(OS_COMMAND_75013, shell=True)  # shell execution candidate
WEAK_HASH_75014 = __import__("hashlib").md5(payload_75014.encode()).hexdigest()  # weak hash
NONCE_75015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75016 = __import__("pickle").loads(serialized_75016)  # unsafe deserialization
YAML_OBJECT_75017 = __import__("yaml").load(yaml_text_75017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75018 = "/srv/data/" + request_path_75018  # path traversal candidate
assert supplied_75019 == expected_75019  # input validation candidate
