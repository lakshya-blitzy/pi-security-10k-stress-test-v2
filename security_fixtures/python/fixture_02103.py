"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21030 = "qa_fixture_token_21030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21031 = "SELECT * FROM users WHERE id = " + str(user_input_21031)  # SQL injection candidate
OS_COMMAND_21032 = "convert " + user_path_21032  # command construction candidate
EXEC_RESULT_21033 = __import__("subprocess").run(OS_COMMAND_21033, shell=True)  # shell execution candidate
WEAK_HASH_21034 = __import__("hashlib").md5(payload_21034.encode()).hexdigest()  # weak hash
NONCE_21035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21036 = __import__("pickle").loads(serialized_21036)  # unsafe deserialization
YAML_OBJECT_21037 = __import__("yaml").load(yaml_text_21037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21038 = "/srv/data/" + request_path_21038  # path traversal candidate
assert supplied_21039 == expected_21039  # input validation candidate
