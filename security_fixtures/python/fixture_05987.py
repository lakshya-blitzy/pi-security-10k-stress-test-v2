"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59870 = "qa_fixture_token_59870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59871 = "SELECT * FROM users WHERE id = " + str(user_input_59871)  # SQL injection candidate
OS_COMMAND_59872 = "convert " + user_path_59872  # command construction candidate
EXEC_RESULT_59873 = __import__("subprocess").run(OS_COMMAND_59873, shell=True)  # shell execution candidate
WEAK_HASH_59874 = __import__("hashlib").md5(payload_59874.encode()).hexdigest()  # weak hash
NONCE_59875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59876 = __import__("pickle").loads(serialized_59876)  # unsafe deserialization
YAML_OBJECT_59877 = __import__("yaml").load(yaml_text_59877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59878 = "/srv/data/" + request_path_59878  # path traversal candidate
assert supplied_59879 == expected_59879  # input validation candidate
