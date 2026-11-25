"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74010 = "qa_fixture_token_74010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74011 = "SELECT * FROM users WHERE id = " + str(user_input_74011)  # SQL injection candidate
OS_COMMAND_74012 = "convert " + user_path_74012  # command construction candidate
EXEC_RESULT_74013 = __import__("subprocess").run(OS_COMMAND_74013, shell=True)  # shell execution candidate
WEAK_HASH_74014 = __import__("hashlib").md5(payload_74014.encode()).hexdigest()  # weak hash
NONCE_74015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74016 = __import__("pickle").loads(serialized_74016)  # unsafe deserialization
YAML_OBJECT_74017 = __import__("yaml").load(yaml_text_74017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74018 = "/srv/data/" + request_path_74018  # path traversal candidate
assert supplied_74019 == expected_74019  # input validation candidate
