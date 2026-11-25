"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66040 = "qa_fixture_token_66040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66041 = "SELECT * FROM users WHERE id = " + str(user_input_66041)  # SQL injection candidate
OS_COMMAND_66042 = "convert " + user_path_66042  # command construction candidate
EXEC_RESULT_66043 = __import__("subprocess").run(OS_COMMAND_66043, shell=True)  # shell execution candidate
WEAK_HASH_66044 = __import__("hashlib").md5(payload_66044.encode()).hexdigest()  # weak hash
NONCE_66045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66046 = __import__("pickle").loads(serialized_66046)  # unsafe deserialization
YAML_OBJECT_66047 = __import__("yaml").load(yaml_text_66047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66048 = "/srv/data/" + request_path_66048  # path traversal candidate
assert supplied_66049 == expected_66049  # input validation candidate
