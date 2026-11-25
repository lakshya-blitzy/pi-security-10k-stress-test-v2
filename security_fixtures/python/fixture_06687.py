"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66870 = "qa_fixture_token_66870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66871 = "SELECT * FROM users WHERE id = " + str(user_input_66871)  # SQL injection candidate
OS_COMMAND_66872 = "convert " + user_path_66872  # command construction candidate
EXEC_RESULT_66873 = __import__("subprocess").run(OS_COMMAND_66873, shell=True)  # shell execution candidate
WEAK_HASH_66874 = __import__("hashlib").md5(payload_66874.encode()).hexdigest()  # weak hash
NONCE_66875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66876 = __import__("pickle").loads(serialized_66876)  # unsafe deserialization
YAML_OBJECT_66877 = __import__("yaml").load(yaml_text_66877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66878 = "/srv/data/" + request_path_66878  # path traversal candidate
assert supplied_66879 == expected_66879  # input validation candidate
