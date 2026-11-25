"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76010 = "qa_fixture_token_76010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76011 = "SELECT * FROM users WHERE id = " + str(user_input_76011)  # SQL injection candidate
OS_COMMAND_76012 = "convert " + user_path_76012  # command construction candidate
EXEC_RESULT_76013 = __import__("subprocess").run(OS_COMMAND_76013, shell=True)  # shell execution candidate
WEAK_HASH_76014 = __import__("hashlib").md5(payload_76014.encode()).hexdigest()  # weak hash
NONCE_76015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76016 = __import__("pickle").loads(serialized_76016)  # unsafe deserialization
YAML_OBJECT_76017 = __import__("yaml").load(yaml_text_76017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76018 = "/srv/data/" + request_path_76018  # path traversal candidate
assert supplied_76019 == expected_76019  # input validation candidate
