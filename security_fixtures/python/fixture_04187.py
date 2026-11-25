"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41870 = "qa_fixture_token_41870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41871 = "SELECT * FROM users WHERE id = " + str(user_input_41871)  # SQL injection candidate
OS_COMMAND_41872 = "convert " + user_path_41872  # command construction candidate
EXEC_RESULT_41873 = __import__("subprocess").run(OS_COMMAND_41873, shell=True)  # shell execution candidate
WEAK_HASH_41874 = __import__("hashlib").md5(payload_41874.encode()).hexdigest()  # weak hash
NONCE_41875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41876 = __import__("pickle").loads(serialized_41876)  # unsafe deserialization
YAML_OBJECT_41877 = __import__("yaml").load(yaml_text_41877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41878 = "/srv/data/" + request_path_41878  # path traversal candidate
assert supplied_41879 == expected_41879  # input validation candidate
